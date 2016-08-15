from typing import TypeVar, Callable, Tuple
from functools import reduce

from tryp import maybe, List
from tryp.func import curried
from tryp.lazy import lazy
from tryp.tc.monad import Monad
from tryp.tc.base import ImplicitInstances, tc_prop
from tryp.tc.traverse import Traverse
from tryp.tc.applicative import Applicative
from tryp.tc.foldable import Foldable
from tryp.list import flatten

A = TypeVar('A', covariant=True)
B = TypeVar('B')


class ListInstances(ImplicitInstances):

    @lazy
    def _instances(self):
        from tryp import Map
        return Map(
            {
                Monad: ListMonad(),
                Traverse: ListTraverse(),
                Foldable: ListFoldable(),
            }
        )


class ListMonad(Monad):

    def pure(self, b: B) -> List[B]:
        return List(b)

    def flat_map(self, fa: List[A], f: Callable[[A], List[B]]) -> List[B]:
        return List.wrap(flatten(map(f, fa)))


class ListTraverse(Traverse):

    def traverse(self, fa: List[A], f: Callable, tpe: type):
        monad = Applicative[tpe]
        def folder(z, a):
            return monad.map2(z.product(f(a)), lambda l, b: l.cat(b))
        return fa.fold_left(monad.pure(List()))(folder)


class ListFoldable(Foldable):

    @tc_prop
    def with_index(self, fa: List[A]) -> List[Tuple[int, A]]:
        return List.wrap(enumerate(fa))

    def filter(self, fa: List[A], f: Callable[[A], bool]):
        return List.wrap(filter(f, fa))

    @curried
    def fold_left(self, fa: List[A], z: B, f: Callable[[B, A], B]) -> B:
        return reduce(f, fa, z)

    def find_map(self, fa: List[A], f: Callable[[A], maybe.Maybe[B]]
                 ) -> maybe.Maybe[B]:
        for el in fa:
            found = f(el)
            if found.is_just:
                return found
        return maybe.Empty()

    def index_where(self, fa: List[A], f: Callable[[A], bool]):
        gen = (maybe.Just(i) for i, a in enumerate(fa) if f(a))
        return next(gen, maybe.Empty())  # type: ignore

__all__ = ('ListInstances',)
