% a script file for testing how fast the circle.m is

clear all;

M = 600
N = 800

maxR = 300;
minR = 10;

%torus = 0
%num = 1     % original circle without torus, ~18s MI VITT
%torus = 0;
%num = 1000;     % original circle without torus, ~20s
%torus = 1;
%num = 1000;     % original circle with torus, ~2m18s

%torus =0
%num = 100      % new circle without torus, ~1.6 s
%torus = 0
%num = 1000      % new circle without torus, ~14s
torus = 1
num = 1000      % new circle with torus, ~40s

testPtsX = floor(M.*rand(1, num));
testPtsY = floor(N.*rand(1, num));
testRs = floor((maxR - minR).*rand(1, num)) + minR;

disp('test circles generated')

for k = 1:num
    % testing original without torus
    c = newcircle(testPtsX(k), testPtsY(k), testRs(k), [M, N], torus);
end

disp('done')
disp(num)
