function y = namecorrect(n,inputpath)
    
S = dir(fullfile(inputpath,'*.png'));
S = S(~[S.isdir]);
filename_size = 6;
for i = 1 : length(S)
    if length(S(i).name)<filename_size
        [~,f,ext]=fileparts(S(i).name);
        rename = strcat('0',f,ext);
        movefile(S(i).name,rename);
    end
end

        