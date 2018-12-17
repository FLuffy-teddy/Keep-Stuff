##########----README----##########
A = (x, y, z, 3)
R = ((x, x), (y, y), (z, z), (3, 3))
A = (x, y)
R = ((x, y), (y, x), (x, x))
A = (x, y, z)
R = ((x, y), (y, z) (z, x))
A = (x, y, z)
R = ((x, x), (x, y), (x,y))
A = (x, y, z)
R = ((x, z), (y, z), (z,y))
A = (x, y, z)
R = ((x, z), (z, y), (y, x))

I have a total of 6 combinations that each show different sets of relations
Reflexive = R; Symmetric = S; Transitive = T; AntiSymmetric = AS
1.)R, S, T, AS
2.)nR, S, nT, AS
3.)nR, nS, nT, AS
4.)nR, nS, T, AS
5.)nR, nS, T, AS
6.)nR, nS, nT, AS

A bug I noticed is with the AntiSymmetric function in which the function result from the output could be shown an error from the rels.py file, saying it is producing an error on line 133 which is the line producing the output file to read the result. Don't know what is causing the issue.

TODOs 
I need to simplify the code for the functions to make them run smoother and more efficiently without all the unneccesary loop functions that slow down larger input files.
I also need to expand the AntiSymmetric function code to make it run without the error on line 133 as mentioned above.
