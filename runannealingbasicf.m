% test run: basic version of annealing
% (fine level of detail, each state stored)

datapics_mat = 'testdata-shared/testdatapics.mat'

% name of this scenario
basename = 'basicf'

% set up annSettings struct
% size of the 'ensemble'
% i.e. the number of annealing algorithms run per testdata
annSettings.ensembleSize = 100;

annSettings.temperature = @(told) basictemperature(told, 0.98);
annSettings.transition  = @(x,y,r,N,M) basictransition(x,y,r,N,M, max(M/15, N/15));
annSettings.cost        = @(x,y,r,data) basiccost(x,y,r,data,0,1);

runannealing(datapics_mat, basename, annSettings, 1);
