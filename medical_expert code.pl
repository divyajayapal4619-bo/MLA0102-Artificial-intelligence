%%writefile medical_expert.pl

:- dynamic symptom/1.

% ----------------------------------------
% EXPERIMENT 17: MEDICAL EXPERT SYSTEM
% ----------------------------------------

% Disease rules

disease(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(body_pain),
    symptom(fatigue).

disease(common_cold) :-
    symptom(cough),
    symptom(runny_nose),
    symptom(sneezing),
    symptom(sore_throat).

disease(malaria) :-
    symptom(fever),
    symptom(chills),
    symptom(sweating),
    symptom(headache).

disease(dengue) :-
    symptom(fever),
    symptom(headache),
    symptom(body_pain),
    symptom(skin_rash).

disease(pneumonia) :-
    symptom(fever),
    symptom(cough),
    symptom(chest_pain),
    symptom(breathing_difficulty).

% ----------------------------------------
% Diagnosis
% ----------------------------------------

diagnose :-
    write('=============================='), nl,
    write('     MEDICAL EXPERT SYSTEM'), nl,
    write('=============================='), nl,
    write('Patient symptoms:'), nl,
    list_symptoms,
    nl,
    write('Possible diagnosis: '),
    (
        disease(Disease)
        ->
        write(Disease)
        ;
        write('No matching disease found')
    ),
    nl.

% Display symptoms

list_symptoms :-
    symptom(S),
    write('- '),
    write(S),
    nl,
    fail.

list_symptoms.