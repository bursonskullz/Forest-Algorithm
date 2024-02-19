% TITLE: Numerical Evaluation of belmanns forest problem
% AUTHORS: R. BURSON
% DATE: 2-12-2024

% PURPOSE: OBTAIN VISUAL GRAPHICS FOR belmanns report
data = load('escape_path.txt');
domain = load('boundaryplot.txt')

figure(1)
plot(data(:,1),data(:,2),'linewidth', 2.5); hold on;
plot(domain(:,1),domain(:,2),'linewidth', 2.5); hold on;
legend('E(p_0)', '\partial \Omega');
xlabel('x coordinate'); 
[hleg, hobj] = legend;
#set(hleg,'Location','best','NumColumns',2,'FontSize',8);
%set(h, "Location", 'Best');
%%%%%%%%%