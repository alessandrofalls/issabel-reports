Active Directory – Lista de Usuários com PowerShell (HTML, CSV e E-mail)

# Descrição
Com este script é possível extrair todas as propriedades de um usuário do Active Directory além de receber um relatório por via e-mail.

Certamente com este relatório a administração e os controles sobre os usuários do Active Directory ficaram mais eficientes evitando que você tenha surpresas durante uma Auditoria de TI.

# Relatório em HTML
![](http://www.100security.com.br/wp-content/uploads/2016/09/ad-lista04.jpg)

Fonte: http://www.100security.com.br/ad-lista

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
13/02/2020
O script acima foi apenas utilizado como base de consulta para criação de um novo script.

Passo a passo do processo:

1. Criação do arquivo em power shell para buscar a lista dos usuários: lista.ps
	Import-Module ActiveDirectory
	Get-ADUser -properties msRTCSIP-Line,company,department,Title -filter 'Company -like "*Sicredi União PR/SP*" -and Enabled -eq $True' | Select-object Name,Department,msRTCSIP-Line,Title | Export-Csv lista.csv -Encoding UTF8
	
2. Note o comando ao final, após o segundo PIPE, exportando diretamente para CSV a saída, dentro dos parâmetros do primeiro PIPE.
3. Copiar 
3. Exportar o CSV para o banco de dados que, neste caso, será utilizado o MongoDB na nuvem, através do Mogo Atlas: https://www.mongodb.com/ (pode ser utilizado a conta gratuita para armazenamento até 512MB)
