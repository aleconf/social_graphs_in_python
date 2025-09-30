# Description

The file `SocialNetwork.txt` represents an imaginary social network of people. Each line in the file provides the names of two people who are friends. Note that the graph associated to the social network is undirected, i.e. if A is a friend of B then B is a also friend of A, hence if `A,B` is a line in the file, there is no need to have the line `B,A`.

The Python file computes the following data:
1. the total number of people in the social network;
2. the distance between two chosen people A and B, where the distance between two members of the network is defined as the minimum number of ties required to connect the two people in the social network;
3. an example of a minimal path between A and B.

The purpose of this exercise is to use only the core Python language, avoiding any library at all. Namely:
- `import` statements are forbidden;
- string method `.split()` is also forbidden.
