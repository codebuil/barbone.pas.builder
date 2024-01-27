Library kernel;
uses 
    libU;
procedure mains;cdecl;
var
            p: PChar ='hello world \n';

begin
        clear();
        locate(10,10);
        print(p);
               
               
end;
exports 
mains;
end.
