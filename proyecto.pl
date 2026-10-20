%primer_semestre_matutino.
%consulta(Semestre, Profe, Materia, Turno).
consulta(1,'FIGUEROA DEL PRADO FELIPE DE JESUS','fundamentos de programacion',matutino).
consulta(1,'SUAREZ CASTAÑON MIGUEL','fundamentos de programacion',matutino).
consulta(1,'GUTIERREZ LUQUE DIANA','comunicacion oral y escrita',matutino).
consulta(1,'VAZQUEZ ARREGUIN ROBERTO','calculo',matutino).
consulta(1,'SALINAS HERNANDEZ ENCARNACION','mecanica y electromagnetismo',matutino).
consulta(1,'MARTINEZ PERALES JOSE CRUZ','fundamentos economicos',matutino).
consulta(1,'JIMENEZ VILLANUEVA MARTHA PATRICIA','matematicas discretas',matutino).
consulta(1,'CENTENO ARRAZOLA MARIA SOLEDAD','comunicacion oral y escrita',matutino).
consulta(1,'OJEDA GUILLEN DIDIER','calculo',matutino).
consulta(1,'MUÑOZ SALAZAR LAURA','mecanica y electromagnetismo',matutino).
consulta(1,'SANCHEZ CRUZ VIRGINIA','fundamentos economicos',matutino).
%primer_semestre_vespertino.
consulta(1,'DE LA O TORRES SAUL','fundamentos de programacion',vespertino).
consulta(1,'GUTIERREZ GARCIA JUAN JESUS','fundamentos de programacion',vespertino).
consulta(1,'DORANTES CORDERO MARTHA MARGARITA','comunicacion oral y escrita',vespertino).
consulta(1,'FLORES MERAZ YESICA SONIA','calculo',vespertino).
consulta(1,'LEVARIO MEDINA SERGIO','mecanica y electromagnetismo',vespertino).
consulta(1,'ESTRADA ELIZALDE SERAFIN','fundamentos economicos',vespertino).

consulta(1,'LUCIO PEÑA PERLA CECILIA','matematicas discretas',vespertino).
consulta(1,'NAVA LARA JOEL','matematicas discretas',vespertino).
consulta(1,'GOMEZ TRESS MARIANA','comunicacion oral y escrita',vespertino).
consulta(1,'LEVARIO MEDINA SERGIO','calculo',vespertino).
consulta(1,'CRUZ ROJAS JORGE ALBERTO','mecanica y electromagnetismo',vespertino).
consulta(1,'MARTINEZ PERALES JOSE CRUZ','fundamentos economicos',vespertino).
%segundo_semestre_matutino.
consulta(2,'RUEDA MELENDEZ JOSE MARCO ANTONIO','algoritmos y estructuras de datos',matutino).
consulta(2,'GONZALEZ CISNEROS ALEJANDRO','algebra lineal',matutino).
consulta(2,'AGUILAR SANCHEZ FERNANDO','fundamentos de diseño digital',matutino).
consulta(2,'HERNANDEZ VASQUEZ CESAR','calculo multivariable',matutino).
consulta(2,'VERA HERNANDEZ GUMERSINDO','ingenieria, etica y sociedad',matutino).
consulta(2,'HERNANDEZ JAIME JOSEFINA','finanzas empresariales',matutino).

consulta(2,'ALBORTANTE MORATO CECILIA','algoritmos y estructuras de datos',matutino).
consulta(2,'LOPEZ SANCHEZ JOSE MANUEL','algebra lineal',matutino).

%segundo_semestre_vespertino.
consulta(2,'RAMIREZ ROMERO TONAHTIU ARTURO','algoritmos y estructuras de datos',vespertino).
consulta(2,'LEAL PACHECO CHRISTIAN RENE','algebra lineal',vespertino).
consulta(2,'BARRON VERA JOSUE EMANUEL','fundamentos de diseño digital',vespertino).
consulta(2,'ZARATE CARDENAS ALEJANDRO','calculo multivariable',vespertino).
consulta(2,'OLALDE MOGOLLAN NORMA','ingenieria, etica y sociedad',vespertino).
consulta(2,'ESTRADA ELIZALDE SERAFIN','finanzas empresariales',vespertino).

consulta(2,'SANTIAGO VALENTIN ERIC','algebra lineal',vespertino).
consulta(2,'LEON HERNANDEZ MIGUEL ABEL','calculo multivariable',vespertino).

%filtro1_profesor.
 %filtro1_profesor(Materia, Profe1,Profe2, Turno).
 filtro1_profesor(Materia, Profe1,profe2, Turno) :-
 consulta(_,Profe1, Materia,Turno),
 consulta(_,Profe2,Materia,Turno),
 Profe1 \= Profe2.

%materias_por_semestre.
 %materias_por_semestre(Semestre,Materia1,Materia2).
 materias_por_semestre(Semestre,Materia1,Materia2) :-
 consulta(Semestre,_,Materia1,_),
 consulta(Semestre,_,Materia2,_),
 Materia1 \= Materia2.

%materia_ambos_turnos.
 %materia_ambos_turnos(Materia).
 materia_ambos_turnos(Materia) :-
 consulta(_,_, Materia, matutino),
 consulta(_,_, Materia, vespertino).

%materia_seriada_1.
 %materia_seriada_1(Materia1, Semestre1, Materia2, Semestre2).
 materia_seriada_1(Materia1, Semestre1, Materia2, Semestre2) :-
 consulta(Semestre1,_,Materia1,_),
 consulta(Semestre2,_,Materia2,_),
 Semestre1 < Semestre2,
 Materia1 \= Materia2.

%mismo_semestre.
 %mismo_semestre(Materia1, Materia2,Semestre).
 mismo_semestre(Materia1, Materia2,Semestre):-
 consulta(Semestre,_,Materia1,_),
 consulta(Semestre,_,Materia2,_).

%filtro_turno.
 %filtro_turno(Semestre,Profe1,Profe2).
 filtro_turno(Semestre,Profe1,Profe2):-
 consulta(Semestre,Profe1,Materia,_),
 consulta(Semestre,Profe2,Materia,_).


%Predicados.

%todos_profesores.
%todos_profesores(Semestre,Lista).
todos_profesores(Semestre,Lista) :-
setof(Profe, Turno^Materia^consulta(Semestre,Profe,Materia,Turno),Lista).

%seriacion_avanzada(Materia1,Materia2, Materia3).
seriacion_avanzada(Materia1, Materia2) :-
 materia_seriada_1(Materia1, Semestre1, Materia2, Semestre2), 
 Semestre1 < Semestre2.

seriacion_avanzada(Materia1,Materia3) :-
 materia_seriada_1(Materia1,_,Materia2,_),
 seriacion_avanzada(Materia2, Materia3).

