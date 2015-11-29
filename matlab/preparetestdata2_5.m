% create test data images

% stored in the folder testdata-shared

% image size
N = 50;

datasetname = 'testdata2_5'

picSets = {};
% params for test pics

radii_series_2 = 2.^(1:1:4)
rn2 = length(radii_series_2);

% 5 circles, one of them changes

for p1 = 1:1:rn2
    picSets{p1} = [10 10 3; 38 48 4; 40 12 6; 12 34 8; 25 25 radii_series_2(p1)];
end

prepare(picSets, N, ['testdata-shared/', datasetname, '.mat'], ['testdata-images/', datasetname,'-pic-'], 1)
