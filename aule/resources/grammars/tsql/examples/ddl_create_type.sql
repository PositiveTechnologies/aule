-- https://docs.microsoft.com/en-us/sql/t-sql/statements/create-type-transact-sql

--#begin
-- Creating an alias type based on the varchar data type
--CREATE TYPE SSN
--FROM varchar(11) NOT NULL ;
--#end
--#begin
-- Creating a user-defined type
--CREATE ASSEMBLY utf8string
--AUTHORIZATION [dbi]
--FROM 0x4D... ;
--GO
--CREATE TYPE Utf8String
--EXTERNAL NAME utf8string.[Microsoft.Samples.SqlServer.utf8string] ;
--GO
--#end
--#begin
-- Creating a user-defined table type
--CREATE TYPE LocationTableType AS TABLE
--    ( LocationName VARCHAR(50)
--    , CostRate INT );
--GO
--#end