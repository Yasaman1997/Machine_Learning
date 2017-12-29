t=[0:0.01:0.98]
y1=sin(2*pi*4*t)
plot(t,y1)

y2=cos(2*pi*4*t)
plot(t,y2)



 plot(t,y1)
 hold on
 plot(t,y2)
 
 xlabel('time')
 ylabel('value')
 
 legend('sin','cos')
 title('my plot')
 
 
 print -dpng 'myplot.png'
 
 
 figure(1):plot(t,y1)
 title('sin')
 xlabel('time')
 ylabel('value')
 
 figure(2):plot(t,y2)
 title('cos')
 xlabel('time')
 ylabel('value')
 
 
 
 
 subplot(1,2,1);   %divides plot as 1*2 grid 
 plot(t,y1)
 subplot(1,2,2)
 plot(t,y2)
 
 
 axis([0.5 1 -1 1])
 clf
 
 
 
 A=magic(5)
 
 imagesc(A)
 imagesc(A),colorbar,colormap gray

 imagesc(magic(15)),colorbar,colormap gray
 
 
 a=1
 b=2
 c=3
 
 
 
  
  
  
  