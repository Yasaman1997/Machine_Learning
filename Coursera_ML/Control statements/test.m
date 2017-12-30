v=zeros(10,1)

for i=1:10
  v(i)=2^i;
end;

x=1:10;
for i=x
  disp(i);
 end;
 
 
 i=1;
 while i<=5.
   v(i)=100;
   i=i+1;
 end;
 
 
 i=1;
 while true
   v(i)=999;
   i=i+1;
   if i==6;
     break;
     end;
   end;
   
   
    v(1)=2;
    if v(1)==1;
      disp('the value is one');
    elseif v(1)==2
     disp('value is 2');
    else
   disp('none!');
  end;
  
  
  
  
  
   SquareThisNumber(5)
   
   
   [a,b]=SquareAndCubeThisNumber(5)
   