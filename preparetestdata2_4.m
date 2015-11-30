% create test data images

% stored in the folder testdata-shared

% image size
N = 50;

datasetname = 'testdata2_4'

picSets = {};
% params for test pics

radii_series_2 = 2.^(1:1:4)
rn2 = length(radii_series_2);

% 4 circles, one of them changes

for p1 = 1:1:rn2
    picSets{p1} = [16 44 10; 44 44 8; 44 16 10; 18 18 radii_series_2(p1)];
end

prepare(picSets, N, ['testdata-shared/', datasetname, '.mat'], ['testdata-images/', datasetname,'-pic-'], 1)

