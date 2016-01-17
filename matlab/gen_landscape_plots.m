% gen_landscape_plots.m
% script file to generate some landscape plots
clear;
close all;

N = 50

% plots: golf-hole, naive energy function
%plots = 1

plots = 2 % naive and adapted energy fun, demonstrate local mins

if plots == 1
    x = 25
    y = 25
    r = 3


    fh1 = figure()
    clf;

    A_data = createdataimage(x, y, r, N, N);
    save('-v6','golfholedata.mat', 'A_data')
    imagesc(A_data)
    colormap(gray)
    axis("image", "off", "nolabel")

    fh2 = figure()
    clf;

    rr = 3
    E_n = zeros(N,N);
    for xx = 1:N
        for yy = 1:N
            E_n(xx, yy) = basiccost(xx, yy, rr, A_data, 0, 0);
        end
    end
    %surfc(E_n, 'LineWidth', 1);
    surfc(E_n);
    colormap("default")
    title('r = 3')
    FN = findall(fh2,'-property','FontName');
    set(FN,'FontName', '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf')
    FS = findall(fh2,'-property','FontSize');
    set(FS,'FontSize',8);

    dpi = get (0, "screenpixelsperinch");
    pos = get (gcf, "position");
    papersize = pos(3:4)./dpi;
    set (gcf, "papersize", papersize)
    set (gcf, "paperposition", [0, 0, papersize])


    fh3 = figure()
    clf;
    rr = 5
    E_n_10 = zeros(N,N);
    for xx = 1:N
        for yy = 1:N
            E_n_10(xx, yy) = basiccost(xx, yy, rr, A_data, 0, 0);
        end
    end
    %surfc(E_n_10, 'LineWidth', 1);
    surfc(E_n_10);
    title('r = 5')

    FN = findall(fh3,'-property','FontName');
    set(FN,'FontName', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
    FS = findall(fh3,'-property','FontSize');
    set(FS,'FontSize',8);

    dpi = get (0, "screenpixelsperinch");
    pos = get (gcf, "position");
    papersize = pos(3:4)./dpi;
    set (gcf, "papersize", papersize)
    set (gcf, "paperposition", [0, 0, papersize])


    print(fh1, 'golfhole1.png', '-dpng', '-r600')
    print(fh1, 'golfhole1.pdf', '-dpdf')


    print(fh2, 'golfhole2.png', '-dpng', '-r600')
    print(fh2, 'golfhole2.pdf', '-dpdf')

    print(fh3, 'golfhole3.png', '-dpng', '-r600')
    print(fh3, 'golfhole3.pdf', '-dpdf')

elseif plots == 2

    x = [35, 10]
    y = [20, 30]
    r = [15, 5]

    x2 = 34
    y2 = 22
    r2 = 14


    fh1 = figure()
    clf;

    A_data = createdataimage(x, y, r, N, N);
    save('-v6', 'localmindata.mat', 'A_data')
    imagesc(A_data)
    colormap(gray)
    %axis("image", "off", "nolabel")
    axis("image")

    FN = findall(fh1,'-property','FontName');
    set(FN,'FontName', '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf')

    fh2 = figure()
    clf;

    rr = 5
    E_n = zeros(N,N);
    for xx = 1:N
        for yy = 1:N
            E_n(xx, yy) = basiccost([x2 xx], [y2 yy], [r2 rr], A_data, 0, 0);
        end
    end
    %surfc(E_n, 'LineWidth', 1);
    surfc(E_n);
    colormap("default")
    title('r = 5')
    FN = findall(fh2,'-property','FontName');
    set(FN,'FontName', '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf')
    FS = findall(fh2,'-property','FontSize');
    set(FS,'FontSize',8);

    dpi = get (0, "screenpixelsperinch");
    pos = get (gcf, "position");
    papersize = pos(3:4)./dpi;
    set (gcf, "papersize", papersize)
    set (gcf, "paperposition", [0, 0, papersize])


    fh3 = figure()
    clf;

    rr = 8
    E_n2 = zeros(N,N);
    for xx = 1:N
        for yy = 1:N
            E_n2(xx, yy) = basiccost([x2 xx], [y2 yy], [r2 rr], A_data, 0, 0);
        end
    end
    %surfc(E_n2, 'LineWidth', 1);
    surfc(E_n2);
    colormap("default")
    title('r = 8')
    FN = findall(fh3,'-property','FontName');
    set(FN,'FontName', '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf')
    FS = findall(fh3,'-property','FontSize');
    set(FS,'FontSize',8);

    dpi = get (0, "screenpixelsperinch");
    pos = get (gcf, "position");
    papersize = pos(3:4)./dpi;
    set (gcf, "papersize", papersize)
    set (gcf, "paperposition", [0, 0, papersize])

    fh4 = figure()
    clf;

    rr = 5
    E_a = zeros(N,N);
    d = 0
    for xx = 1:N
        for yy = 1:N
            E_a(xx, yy) = basiccost([x2 xx], [y2 yy], [r2 rr], A_data, 0, 1);
            d = d + abs(E_a(xx, yy) - E_n(xx, yy));
        end
    end
    %surfc(E_a, 'LineWidth', 1);
    disp('parannus')
    disp(d)
    surfc(E_a);
    colormap("default")
    title('r = 5')
    FN = findall(fh4,'-property','FontName');
    set(FN,'FontName', '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf')
    FS = findall(fh4,'-property','FontSize');
    set(FS,'FontSize',8);

    dpi = get (0, "screenpixelsperinch");
    pos = get (gcf, "position");
    papersize = pos(3:4)./dpi;
    set (gcf, "papersize", papersize)
    set (gcf, "paperposition", [0, 0, papersize])


    fh5 = figure()
    clf;

    rr = 8
    E_a2 = zeros(N,N);
    for xx = 1:N
        for yy = 1:N
            E_a2(xx, yy) = basiccost([x2 xx], [y2 yy], [r2 rr], A_data, 0, 1);
        end
    end
    %surfc(E_a2, 'LineWidth', 1);
    surfc(E_a2);
    colormap("default")
    title('r = 8')
    FN = findall(fh5,'-property','FontName');
    set(FN,'FontName', '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf')
    FS = findall(fh5,'-property','FontSize');
    set(FS,'FontSize',8);

    dpi = get (0, "screenpixelsperinch");
    pos = get (gcf, "position");
    papersize = pos(3:4)./dpi;
    set (gcf, "papersize", papersize)
    set (gcf, "paperposition", [0, 0, papersize])



    print(fh1, 'localmins1.png', '-dpng', '-r600')

    print(fh2, 'localmins2.png', '-dpng', '-r600')
    print(fh2, 'localmins2.pdf', '-dpdf')

    print(fh3, 'localmins3.png', '-dpng', '-r600')
    print(fh3, 'localmins3.pdf', '-dpdf')

    print(fh4, 'localmins4.png', '-dpng', '-r600')
    print(fh4, 'localmins4.pdf', '-dpdf')

    print(fh5, 'localmins5.png', '-dpng', '-r600')
    print(fh5, 'localmins5.pdf', '-dpdf')
end
