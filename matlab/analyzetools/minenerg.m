clear all;
load('testdata-annealingbasicf/ann-data-pic-3')
load('testdata-shared/testdatapics')
load('testdata-annealingbasicf/results-pic-3')

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


xa = enX{meind}
ya = enY{meind}
ra = enR{meind}

figure(1)
clf;
imshow(A_data)
hold on;
% plot the SA result circle
plot(ya, xa, 'r+', 'linewidth', 2)
rt = linspace(0, 2*pi, 100);
for circ = 1:length(ya)
    plot(ra(circ)*sin(rt) + ya(circ), ra(circ)*cos(rt) + xa(circ), 'r', 'linewidth', 3);
end

axis image
title('The best SA result from an ensemble of 100 runs', 'fontsize', 15)
print('best-result-pic-octave-3.png', '-dpng')

figure(2)

clf;
hold on;
plot(1:100, bestEnergies, 'b', 'linewidth', 2);
plot(1:100, finalEnergies, 'k-d', 'markersize', 7, 'linewidth', 1)
title('The final energies in an ensemble of 100 runs', 'fontsize', 15);
legend('Best energy so far', 'Final energy of a run')
print('ens-energy-plot-pic-octave-3.png', '-dpng')
ylabel('Energy')
xlabel('Walker no.')

figure(3)

clf;
[sortedEnergies, sortedInd] = sort(finalEnergies);

subaxis(4,4,1, 'Spacing', 0.03, 'SpacingHoriz', 0.06, 'Padding', 0.02, 'Margin', 0.05);
imshow(A_data)
title('Data')
for k = 2:16
    subaxis(4,4,k, 'Spacing', 0.03, 'SpacingHoriz', 0.06, 'Padding', 0.02, 'Margin', 0.05);
    hold on;
    imshow(A_data)
    kind = sortedInd(k-1);
    xa = enX{kind};
    ya = enY{kind};
    ra = enR{kind};
    plotrescircles(xa, ya, ra)
    axis tight
    title(['E= ', num2str(sortedEnergies(k-1))])

end

figure(4)
clf;

energies = enDataEnerg{meind};
temps = enDataTemps{meind};
l = length(energies)
[ax, p1, p2] = plotyy(1:l, energies, 1:l, temps)
%set([p1, p2], 'linewidth', 1)
title('Energy of the best walker')
ylabel(ax(1), 'Energy')
ylabel(ax(2), 'Temperature')
xlabel('Step')
print('best-energy-temp-pic-octave-3.png', '-dpng')

figure(5)
clf;


points = enDataPts{meind};
radii = enDataR{meind};
for s = [1, 500, 1000, 1500, 2000, l]
    clf;
    hold on;
    imshow(A_data)
    x = points(1,s,:);
    y = points(2,s,:);
    r = radii(s, :);
    plotrescircles(x, y, r)
    title(['Best walker: Step = ', num2str(s), ' Energy = ', num2str(energies(s))])
    print(['progress-step-', num2str(s), 'pic-octave-3.png'], '-dpng')
end
