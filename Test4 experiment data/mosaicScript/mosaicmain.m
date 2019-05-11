clc;
clear;
y = namecorrect(6,pwd);
D=dir('*.png');
fnum=length(D);
n=input('row number:'); % row number
m=floor(fnum/n);
height = 1216;
width = 1936;
scale = 0.125;
imt=zeros(floor(height*n*scale),floor(width*m*scale),3);
imt = uint8(imt);
id=1;
 for l=1:n
    
    for k = 1:m
        ima=imread(D(id).name);
        ima = imresize(ima,scale);
        if mod(l,2)==1
        imt((scale*height*(n-l)+1):scale*height*(n-l+1),scale*width*(m-k)+1:scale*width*(m-k+1),:)=ima(:,:,:);
        else 
        imt((scale*height*(n-l)+1):scale*height*(n-l+1),scale*width*(k-1)+1:scale*width*k,:)=ima(:,:,:);
        end
        id=id+1;
    end
    
 end
 
 imshow(imt);