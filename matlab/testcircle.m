% a script file for testing that the function CIRCLE works correctly

close all;
clear all;

% fix the image matrix size

N = 200
M = 400

% define known circle param sets for test cases
% (x, y, radius)

test1 = [25, 50, 100]

simpleIm1 = circle(num2cell(test1){:}, [N, M], 0);
figure(1)
imagesc(simpleIm1)

torusIm1 = circle(num2cell(test1){:}, [N, M], 1);
figure(2)
imagesc(torusIm1)

newSimpleIm = newcircle(num2cell(test1){:}, [N, M], 0);
figure(3)
imagesc(newSimpleIm)

newTorusIm = newcircle(num2cell(test1){:}, [N, M], 1);
figure(4)
imagesc(newTorusIm)
