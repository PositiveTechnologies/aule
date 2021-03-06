-- https://docs.microsoft.com/en-us/sql/t-sql/language-elements/cursors-transact-sql

#begin
-- close
DECLARE Employee_Cursor CURSOR FOR
SELECT EmployeeID, Title FROM AdventureWorks2012.HumanResources.Employee;
OPEN Employee_Cursor;
FETCH NEXT FROM Employee_Cursor;
WHILE @@FETCH_STATUS = 0
   BEGIN
      FETCH NEXT FROM Employee_Cursor;
   END;
CLOSE Employee_Cursor;
DEALLOCATE Employee_Cursor;
GO

#end
#begin
-- DEALLOCATE
USE AdventureWorks2012;
GO
-- Create and open a global named cursor that
-- is visible outside the batch.
DECLARE abc CURSOR GLOBAL SCROLL FOR
    SELECT * FROM Sales.SalesPerson;
OPEN abc;
GO
-- Reference the named cursor with a cursor variable.
DECLARE @MyCrsrRef1 CURSOR;
SET @MyCrsrRef1 = abc;
-- Now deallocate the cursor reference.
DEALLOCATE @MyCrsrRef1;
-- Cursor abc still exists.
FETCH NEXT FROM abc;
GO
-- Reference the named cursor again.
DECLARE @MyCrsrRef2 CURSOR;
SET @MyCrsrRef2 = abc;
-- Now deallocate cursor name abc.
DEALLOCATE abc;
-- Cursor still exists, referenced by @MyCrsrRef2.
FETCH NEXT FROM @MyCrsrRef2;
-- Cursor finally is deallocated when last referencing
-- variable goes out of scope at the end of the batch.
GO
-- Create an unnamed cursor.
DECLARE @MyCursor CURSOR;
SET @MyCursor = CURSOR LOCAL SCROLL FOR
SELECT * FROM Sales.SalesTerritory;
-- The following statement deallocates the cursor
-- because no other variables reference it.
DEALLOCATE @MyCursor;
GO

#end
#begin
-- DECLARE CURSOR. Using simple cursor and syntax
DECLARE vend_cursor CURSOR
    FOR SELECT * FROM Purchasing.Vendor
OPEN vend_cursor
FETCH NEXT FROM vend_cursor;

#end
#begin
-- DECLARE CURSOR. Using nested cursors to produce report output
SET NOCOUNT ON;

DECLARE @vendor_id int, @vendor_name nvarchar(50),
    @message varchar(80), @product nvarchar(50);

PRINT '-------- Vendor Products Report --------';

DECLARE vendor_cursor CURSOR FOR
SELECT VendorID, Name
FROM Purchasing.Vendor
WHERE PreferredVendorStatus = 1
ORDER BY VendorID;

OPEN vendor_cursor

FETCH NEXT FROM vendor_cursor
INTO @vendor_id, @vendor_name

WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT ' '
    SELECT @message = '----- Products From Vendor: ' +
        @vendor_name

    PRINT @message

    -- Declare an inner cursor based
    -- on vendor_id from the outer cursor.

    DECLARE product_cursor CURSOR FOR
    SELECT v.Name
    FROM Purchasing.ProductVendor pv, Production.Product v
    WHERE pv.ProductID = v.ProductID AND
    pv.VendorID = @vendor_id  -- Variable value from the outer cursor

    OPEN product_cursor
    FETCH NEXT FROM product_cursor INTO @product

    IF @@FETCH_STATUS <> 0
        PRINT '         <<None>>'

    WHILE @@FETCH_STATUS = 0
    BEGIN

        SELECT @message = '         ' + @product
        PRINT @message
        FETCH NEXT FROM product_cursor INTO @product
        END

    CLOSE product_cursor
    DEALLOCATE product_cursor
        -- Get the next vendor.
    FETCH NEXT FROM vendor_cursor
    INTO @vendor_id, @vendor_name
END
CLOSE vendor_cursor;
DEALLOCATE vendor_cursor;

#end
#begin
-- FETCH. Using FETCH in a simple cursor
USE AdventureWorks2012;
GO
DECLARE contact_cursor CURSOR FOR
SELECT LastName FROM Person.Person
WHERE LastName LIKE 'B%'
ORDER BY LastName;

OPEN contact_cursor;

-- Perform the first fetch.
FETCH NEXT FROM contact_cursor;

-- Check @@FETCH_STATUS to see if there are any more rows to fetch.
WHILE @@FETCH_STATUS = 0
BEGIN
   -- This is executed as long as the previous fetch succeeds.
   FETCH NEXT FROM contact_cursor;
END

CLOSE contact_cursor;
DEALLOCATE contact_cursor;
GO
#end
#begin
-- FETCH. Using FETCH to store values in variables
USE AdventureWorks2012;
GO
-- Declare the variables to store the values returned by FETCH.
DECLARE @LastName varchar(50), @FirstName varchar(50);

DECLARE contact_cursor CURSOR FOR
SELECT LastName, FirstName FROM Person.Person
WHERE LastName LIKE 'B%'
ORDER BY LastName, FirstName;

OPEN contact_cursor;

-- Perform the first fetch and store the values in variables.
-- Note: The variables are in the same order as the columns
-- in the SELECT statement.

FETCH NEXT FROM contact_cursor
INTO @LastName, @FirstName;

-- Check @@FETCH_STATUS to see if there are any more rows to fetch.
WHILE @@FETCH_STATUS = 0
BEGIN

   -- Concatenate and display the current values in the variables.
   PRINT 'Contact Name: ' + @FirstName + ' ' +  @LastName

   -- This is executed as long as the previous fetch succeeds.
   FETCH NEXT FROM contact_cursor
   INTO @LastName, @FirstName;
END

CLOSE contact_cursor;
DEALLOCATE contact_cursor;
GO

#end
#begin
-- FETCH. Declaring a SCROLL cursor and using the other FETCH options
USE AdventureWorks2012;
GO
-- Execute the SELECT statement alone to show the
-- full result set that is used by the cursor.
SELECT LastName, FirstName FROM Person.Person
ORDER BY LastName, FirstName;

-- Declare the cursor.
DECLARE contact_cursor SCROLL CURSOR FOR
SELECT LastName, FirstName FROM Person.Person
ORDER BY LastName, FirstName;

OPEN contact_cursor;

-- Fetch the last row in the cursor.
FETCH LAST FROM contact_cursor;

-- Fetch the row immediately prior to the current row in the cursor.
FETCH PRIOR FROM contact_cursor;

-- Fetch the second row in the cursor.
FETCH ABSOLUTE 2 FROM contact_cursor;

-- Fetch the row that is three rows after the current row.
FETCH RELATIVE 3 FROM contact_cursor;

-- Fetch the row that is two rows prior to the current row.
FETCH RELATIVE -2 FROM contact_cursor;

CLOSE contact_cursor;
DEALLOCATE contact_cursor;
GO

#end
#begin
-- OPEN
DECLARE Employee_Cursor CURSOR FOR
SELECT LastName, FirstName
FROM AdventureWorks2012.HumanResources.vEmployee
WHERE LastName like 'B%';

OPEN Employee_Cursor;

FETCH NEXT FROM Employee_Cursor;
WHILE @@FETCH_STATUS = 0
BEGIN
    FETCH NEXT FROM Employee_Cursor
END;

CLOSE Employee_Cursor;
DEALLOCATE Employee_Cursor;
#end
