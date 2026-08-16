bird(sparrow).
bird(parrot).
bird(eagle).
bird(pigeon).
bird(penguin).
bird(ostrich).

animal(dog).
animal(cat).

cannot_fly(penguin).
cannot_fly(ostrich).

can_fly(X) :-
    bird(X),
    \+ cannot_fly(X).

is_bird(X) :-
    bird(X).