% function file for prepare

function prepare(picSets, N, datatarget, imagetarget, visibleoff)
    % PREPARE function that generalizes common routines of test data generation
    % prepare(picSets, N, datatarget, imagetarget, visible)
    %
    % PARAMS:
    % picSets: cell array {pic1; pic2; ...; picn} of n target circle matrices
    %   each pic is a matrix [cx1, cy1, cr1; ...; cxd, cyd, crd] of d circles
    % N: size of a pic
    % datatarget: filename to which the data objects are saved
    % imagetarget: common part of filename for target pictures
    %    each pic will be saved at imagetarget1.png, imagetarget2.png, ... etc
    % visibleoff: if true, fighandle = figure('visible', 'off')
    %   (useful for printing pictures on UKKO cluster without X)

    numPics = length(picSets)
    nDataCircles = zeros(1, numPics);

    dataSets = {};

    for picInd = 1:numPics
        if visibleoff
            fighandle = figure('visible', 'off')
        else
            fighandle = figure()
        end
        clf;
        picSet = picSets(picInd);
        picSet = picSet{:}
        nDataCircles(picInd) = length(picSet(:, 1));
        x = picSet(:, 1);
        y = picSet(:, 2);
        r = picSet(:, 3);

        A_data = createdataimage(x, y, r, N, N);
        imagesc(A_data)
        colormap(gray)
        axis image
        dataSets{picInd} = A_data;

        print(fighandle, [imagetarget, num2str(picInd), '.png'], '-dpng')
    end

    save(datatarget, 'picSets', 'dataSets', 'numPics', 'nDataCircles');

end % end function
