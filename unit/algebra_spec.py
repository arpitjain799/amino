from typing import Generic, TypeVar

from amino.test.spec_spec import Spec
from amino.algebra import Algebra
from amino.case import Case
from amino import ADT

A = TypeVar('A')


class Base(Generic[A], ADT['Base']):
    pass


class A1(Generic[A], Base):
    pass


class A2(Generic[A], Base):
    pass


class tostr(Generic[A], Case[Base, str], alg=Base):

    def a1(self, a: A1[A]) -> str:
        return str(a)

    def a2(self, a: A2) -> str:
        return str(a)


class AlgebraSpec(Spec):

    def subclasses(self) -> None:
        print(tostr.match(A1()))


__all__ = ('AlgebraSpec',)