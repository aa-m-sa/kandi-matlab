% A function for running annealing ensemble with params and producing some basic plots
% (fine level of detail, each state stored)

function runannealing(datapics_mat, basename, annSettings, nopause)
    % RUNANNEALING runs an annealing ensemble
    % datapics_mat a file like 'testdata-shared/testdatapics_small.mat'

    load(datapics_mat, 'dataSets', 'numPics', 'nDataCircles');

    dirname = ['testdata-annealing', basename, '/'];

    if ~isdir(dirname)
        mkdir(dirname)
    end

    % size of the 'ensemble'
    % i.e. the number of annealing algorithms run per testdata
    if isfield(annSettings, 'ensembleSize')
        ensembleSize = annSettings.ensembleSize;
    else
        ensembleSize = 100
    end

    disp(nDataCircles)

    if ~nopause
        disp('(paused before starting)')
        pause;
    end

    for kpic = 1:numPics
        %
        A_data = dataSets{kpic};
        nCircles = nDataCircles(kpic);

        energies = zeros(1, ensembleSize);
        bestEnergies = zeros(1, ensembleSize);

        % cell arrays for archiving
        enX = {};
        enY = {};
        enR = {};
        enDataLen = {};
        enDataPts = {};
        enDataR = {};
        enDataEnerg = {};
        enDataTemps = {};
        enDataRatios = {};
        enDataMarkovNo = {};

        parfor e = 1:ensembleSize
            %
            [x, y, r,  ...
            annDataPoints, annDataRadii, annDataEnergies, annDataTemps, ...
            ratios, annDataMarkovNo] = annealing(A_data, nCircles, annSettings);

            annDataLen = length(annDataEnergies);

            % some initial analyzing:
            % keep count of final energies seen so far
            energies(e) = annDataEnergies(annDataLen);

            % archive results in cell arrays
            enX{e} = x;
            enY{e} = y;
            enR{e} = r;

            enDataLen{e} = annDataLen;
            enDataPts{e} = annDataPoints;
            enDataR{e} = annDataRadii;
            enDataEnerg{e} = annDataEnergies;
            enDataTemps{e} = annDataTemps;
            enDataRatios{e} = ratios;
            enDataMarkovNo{e} = annDataMarkovNo;


        end % end parfor

        % best final energies as function of ensemble size
        for e = 1:ensembleSize
            bestEnergies(e) = min(energies(1:e));
        end
        % plot ensemble best energies
        fighandle = figure('visible', 'off')
        clf;
        hist(energies)
        title(['Histogram of final energies of ', num2str(ensembleSize), ' SA walkers'], 'fontsize', 15);
        print(fighandle, [dirname, 'final-energies-histo-pic-' num2str(kpic) '.png'], '-dpng')
        clf;
        plot(1:ensembleSize, bestEnergies, 'linewidth', 3);
        title('The best energy (so far) as function of the ensemble size', 'fontsize', 15);
        print(fighandle, [dirname, 'best-energy-plot-pic-' num2str(kpic) '.png'], '-dpng')

        % get the coordinates corresponding to the best walker in the ensemble and plot corresp pic
        [me, meind] = min(energies);
        xa = enX{meind}
        ya = enY{meind}
        ra = enR{meind}

        clf;
        hold on;

        imagesc(A_data)
        colormap(gray)
        hold on;
        % plot the SA result circle
        plot(ya, xa, 'r.', 'markersize', 3)
        rt = linspace(0, 2*pi, 100);
        for circ = 1:length(ya)
            plot(ra(circ)*sin(rt) + ya(circ), ra(circ)*cos(rt) + xa(circ), 'r', 'linewidth', 1);
        end

        axis image
        title(['The best SA result from the ensemble of ', num2str(ensembleSize)], 'fontsize', 15)
        print(fighandle, [dirname, 'best-result-pic-' num2str(kpic) '.png'], '-dpng')

        hold off;
        close(fighandle)

        % save other results for later analyzing
        resf = [dirname, 'results-pic-', num2str(kpic)];
        anndf = [dirname, 'ann-data-pic-', num2str(kpic)];

        save(resf, 'enX', 'enY', 'enR')
        save(anndf, 'enDataLen', 'enDataPts', 'enDataR', 'enDataEnerg', 'enDataTemps', 'enDataRatios', 'enDataMarkovNo');

    end
end % end function
