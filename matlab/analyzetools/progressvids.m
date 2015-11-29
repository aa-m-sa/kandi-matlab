clear all;
close all;
load('testdata-annealingbasicf/ann-data-pic-3')
load('testdata-shared/testdatapics')
load('testdata-annealingbasicf/results-pic-3')

viddir = 'vid3b/'

finalEnergies = zeros(1, length(enDataEnerg));
bestEnergies = zeros(1, length(enDataEnerg));

A_data = dataSets{3};
for e = 1:length(enDataEnerg)
    energies = enDataEnerg{e};
    l = length(energies);
    finalEnergies(e) = energies(l);
    bestEnergies(e) = min(finalEnergies(1:e));
end

[me, meind] = min(finalEnergies)

energies = enDataEnerg{meind};
temps = enDataTemps{meind};
points = enDataPts{meind};
radii = enDataR{meind};
h = figure()
for s = 1:(l-1)
    hold on;
    imshow(A_data)
    x = points(1,s,:);
    y = points(2,s,:);
    r = radii(s, :);
    plotrescircles(x, y, r)
    title(['Best walker: Step = ', sprintf('%04d', s), ' Energy = ', num2str(energies(s))])

    set(h, 'PaperUnits', 'inches')
    set(h, 'PaperSize', [6, 6])
    set(h, 'PaperPosition', [0, 0, 6, 6])
    print([viddir, sprintf('%04d', s), '.png'], '-dpng')
    close
end
