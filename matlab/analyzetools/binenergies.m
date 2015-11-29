% tool for binning the final energies of the ensemble

load('testdata-annealingbasic/ann-data-pic-7', 'enDataEnerg')
load('testdata-shared/testdatapics', 'dataSets')
load('testdata-annealingbasic/results-pic-7', 'enX', 'enY', 'enR')

finalEnergies = zeros(1, length(enDataEnerg));

for e = 1:length(enDataEnerg)
    energies = enDataEnerg{e};
    l = length(energies);
    finalEnergies(e) = energies(l);
end

% limits handpicked

binEdges = 2000:100:5000;
[binNums, binIdx] = histc(finalEnergies, binEdges);

figure()
hist(finalEnergies)

figure()
bar(binNums)

enXmat = cell2mat(enX)
enYmat = cell2mat(enY)
enRmat = cell2mat(enR)

% with this data, the interesting bins are 7, 10, 20

bin7xs = enXmat(:, binIdx == 7);
bin7ys = enYmat(:, binIdx == 7);
bin7rs = enRmat(:, binIdx == 7);

figure()
imshow(dataSets{7});
hold on;
for pick = 1:length(bin7xs)
    plotrescircles(bin7xs(:,pick), bin7ys(:,pick), bin7rs(:,pick))
end

bin10xs = enXmat(:, binIdx == 10);
bin10ys = enYmat(:, binIdx == 10);
bin10rs = enRmat(:, binIdx == 10);

figure()
imshow(dataSets{7});
hold on;
for pick = 1:length(bin10xs)
    plotrescircles(bin10xs(:,pick), bin10ys(:,pick), bin10rs(:,pick))
end

bin20xs = enXmat(:, binIdx == 20);
bin20ys = enYmat(:, binIdx == 20);
bin20rs = enRmat(:, binIdx == 20);

figure()
imshow(dataSets{7});
hold on;
for pick = 1:3
    plotrescircles(bin20xs(:,pick), bin20ys(:,pick), bin20rs(:,pick))
end

% interesting! seems that bin no 10 has 'better' circle locations while
% no 7 has better value of energy function

% wait. maybe it's just stacking pics causing inconvenience?
% YES!

for pick = 1:size(bin10xs)
    hold off;
    imshow(dataSets{7})
    hold on;
    plotrescircles(bin10xs(:,pick), bin10ys(:,pick), bin10rs(:,pick))
    pause;
end

% ^ we find that stacking pics together is not the most realiable way to
% analyze the results

% however, it also creates a quite intersting list off all tried cand circles

binBestxs = enXmat(:, binIdx >= 3 & binIdx <=5);

