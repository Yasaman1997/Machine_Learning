A = [1 2; 3 4; 5 6];
B = [1 2 3; 4 5 6];

v = zeros(10, 1);
for i = 1:10
  for j = 1:10
    v(i) = v(i) + A(i, j) * x(j);
  end;
end;





A=[16 2 3 13;5 11 10 8;9 7 6 12;4 14 15 1]

x=zeros(10,1)
A=magic(10)
v = zeros(10, 1);
for i = 1:10
  for j = 1:10
    v(i) = v(i) + A(i, j) * x(j);
  end
end



v=[1:7]
w=[1:7]

z = 0;
for i = 1:7
  z = z + v(i) * w(i)
end




X=[1:7;1:7;1:7;1:7;1:7;1:7;1:7]
for i = 1:7
  for j = 1:7
    A(i, j) = log(X(i, j));
    B(i, j) = X(i, j) ^ 2;
    C(i, j) = X(i, j) + 1;
    D(i, j) = X(i, j) / 4;
  end
end