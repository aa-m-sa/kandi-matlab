% create test data images

% stored in the folder testdata-shared

% image size
N = 200;

% params for test pics
pic1 = [60 120 40];
pic2 = [40 30 20; 150 130 45];
pic3 = [50 50 25; 150 110 40; 80 140 15];
pic4 = [20 30 15; 130 20 10; 90 80 50; 180 170 15];
pic5 = [15 10 5; 160 150 30; 80 50 40; 170 20 10; 70 140 25];
pic6 = [39 59 32; 127 50 16; 26 117 24];
pic7 = [94 47 64; 7 33 21; 151 99 9; 188 172 28];
pic8 = [49 133 12; 62 54 7; 161 188 87; 156 11 49];
pic9 = [186 167 38; 97 140 19; 149 32 46; 146 119 21; 86 69 13];
pic10 = [16 64 32; 56 177 71];
pic11 = [80 66 11];


% 'set' a.k.a. cell array
picSets = {pic1; pic2; pic3; pic4; pic5; pic6; pic7; pic8; pic9; pic10; pic11}

prepare(picSets, N, 'testdata-shared/testdatapics.mat', 'testdata-images/testdata-pic-', 1)

