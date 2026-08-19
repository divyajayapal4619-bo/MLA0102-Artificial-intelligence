%%writefile best_first.pl

% ============================================================
% EXPERIMENT 25
% BEST FIRST SEARCH USING PROLOG
% ============================================================

% ------------------------------------------------------------
% Graph
% ------------------------------------------------------------

edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, d).
edge(c, f).
edge(d, g).
edge(e, g).
edge(f, g).

% ------------------------------------------------------------
% Heuristic values
% Smaller value means closer to goal
% ------------------------------------------------------------

heuristic(a, 10).
heuristic(b, 7).
heuristic(c, 6).
heuristic(d, 4).
heuristic(e, 5).
heuristic(f, 3).
heuristic(g, 0).

% ------------------------------------------------------------
% Best First Search
% ------------------------------------------------------------

best_first(Start, Goal, Path) :-
    search([node(Start, [Start])], Goal, Path).

% Goal reached
search([node(Goal, Path)|_], Goal, Path).

% Continue search
search([node(Current, Path)|Rest], Goal, FinalPath) :-

    findall(
        node(Next, [Next|Path]),
        (
            edge(Current, Next),
            \+ member(Next, Path)
        ),
        Children
    ),

    add_to_queue(Children, Rest, NewQueue),

    sort_queue(NewQueue, SortedQueue),

    search(SortedQueue, Goal, FinalPath).

% ------------------------------------------------------------
% Add children to queue
% ------------------------------------------------------------

add_to_queue([], Queue, Queue).

add_to_queue([H|T], Queue, Result) :-
    add_to_queue(T, [H|Queue], Result).

% ------------------------------------------------------------
% Sort according to heuristic value
% ------------------------------------------------------------

sort_queue(Queue, SortedQueue) :-
    map_list_to_pairs(node_value, Queue, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, SortedQueue).

node_value(node(Node, _), Value) :-
    heuristic(Node, Value).

% ------------------------------------------------------------
% Display Result
% ------------------------------------------------------------

show_result(Start, Goal) :-
    best_first(Start, Goal, ReversePath),
    reverse(ReversePath, Path),
    write('Start Node : '), write(Start), nl,
    write('Goal Node  : '), write(Goal), nl,
    write('Best First Search Path : '),
    write(Path), nl.