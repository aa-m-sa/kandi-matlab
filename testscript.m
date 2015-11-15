% script for testing out functions

clear all;
close all;

% image size
N = 64;

% create image matrix with one circle
% random parameters

% test
%A = circle(80, 80, 42, [N, N]);

x0 = floor(N*rand)
y0 = floor(N*rand)
%r0 = 10 + 50*rand
% test with fixed r0
r0 = 10

A = circle(x0, y0, r0, [N, N]);

% other circles could be added just with A = A + circle(...)

% view image
%imshow(A);

%pause;

I = convolution(A);
%imshow(I);

%pause;

I_noise = addnoise(I);
imshow(I_noise);
hold on;

[xa, ya, ra, aData] = annealing(I_noise, floor(N/2), floor(N/2), r0);

annPlot = flipud(aData);

plot(annPlot(1,:), annPlot(2,:), 'linewidth', 3)
plot(ya, xa, 'r.', 'markersize', 10)
