% run annealing on datasets 2_*
% adjusted version with longer max lens

annSettings_core.ensembleSize = 100
annSettings_core.transition  = @(x,y,r,N,M) basictransition(x,y,r,N,M, max(M/15, N/15));
annSettings_core.cost        = @(x,y,r,data) basiccost(x,y,r,data,0,1);


annSettings_t99_n1000 = annSettings_core;
annSettings_t99_n1000.temp_n      = 1000;
annSettings_t99_n1000.temperature = @(told) basictemperature(told, 0.99);

set2runner(annSettings_t99_n1000, 'set2b-50x50-t99-n1000')


annSettings_t98_n1000 = annSettings_core;
annSettings_t98_n1000.temp_n      = 1000;
annSettings_t98_n1000.temperature = @(told) basictemperature(told, 0.98);

set2runner(annSettings_t98_n1000, 'set2b-50x50-t98-n1000')


annSettings_t96_n600 = annSettings_core;
annSettings_t96_n600.temp_n      = 600;
annSettings_t96_n600.temperature = @(told) basictemperature(told, 0.96);

set2runner(annSettings_t96_n600, 'set2b-50x50-t96-n600')

annSettings_t94_n600 = annSettings_core;
annSettings_t94_n600.temp_n      = 600;
annSettings_t94_n600.temperature = @(told) basictemperature(told, 0.94);

set2runner(annSettings_t94_n600, 'set2b-50x50-t94-n600')

annSettings_t90_n600 = annSettings_core;
annSettings_t90_n600.temp_n      = 600;
annSettings_t90_n600.temperature = @(told) basictemperature(told, 0.90);

set2runner(annSettings_t90_n600, 'set2b-50x50-t90-n600')

