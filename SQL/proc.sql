CREATE PROCEDURE ObterMelhorPrecoPorEmpresa
AS
BEGIN
    WITH MelhoresPrecos AS (
        SELECT Empresa, MIN(CONVERT(NUMERIC(18,2), PrecoTotal)) AS MelhorPreco
        FROM TabelaVoos
        WHERE CONVERT(DATE, DataHoraIda) = CONVERT(DATE, GETDATE()) -- Considerando apenas a data atual
        GROUP BY Empresa
    )
    SELECT TV.Empresa, TV.CompanhiaVoo, TV.PrecoTotal, TV.TaxaEmbarque, TV.TaxaServico, TV.TempoVooMinutos, TV.DataHoraIda, TV.DataHoraVolta
    FROM TabelaVoos TV
    INNER JOIN MelhoresPrecos MP ON TV.Empresa = MP.Empresa AND CONVERT(NUMERIC(18,2), TV.PrecoTotal) = MP.MelhorPreco
    WHERE CONVERT(DATE, TV.DataHoraIda) = CONVERT(DATE, GETDATE()) -- Considerando apenas a data atual
END;