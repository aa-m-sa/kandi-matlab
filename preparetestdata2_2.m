% create test data images

% stored in the folder testdata-shared

% image size
N = 50;

datasetname = 'testdata2_2'

picSets = {};
% params for test pics
% 2 circles, larger steps
radii_series_2 = 2.^(1:1:4)
rn2 = length(radii_series_2);
for p1 = 1:1:rn2
    for p2 = 1:1:rn2
        picSets{(p1-1)*rn2 + p2} = [16 16 radii_series_2(p1); 35 35 radii_series_2(p2)]
    end
end

prepare(picSets, N, ['testdata-shared/', datasetname, '.mat'], ['testdata-images/', datasetname,'-pic-'], 1)

