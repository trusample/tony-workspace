const SPREADSHEET_ID = '1NyYihFTchiur_Nrj5Vz0LSxw1PP4aY6ttctn4G2cT4E';

function doGet(e) {
  return HtmlService.createHtmlOutputFromFile('PortalHTML').setTitle('TruSample CRM');
}

function doPost(e) {
  try {
    const payload = JSON.parse(e.postData.contents);
    const action = payload.action;
    const email = Session.getActiveUser().getEmail();
    const ss = SpreadsheetApp.openById(SPREADSHEET_ID);
    switch(action) {
      case 'getCurrentUser':
        const users = ss.getSheetByName('Users').getDataRange().getValues();
        let role = 'VIEWER';
        for (let i=1;i<users.length;i++) {
          if (String(users[i][0]).toLowerCase()===email.toLowerCase()) { role=users[i][1]; break; }
        }
        return out_({success:true, user:{email:email, role:role}});
      case 'getContacts':
        return out_({success:true, data:sheetToObjects_(ss.getSheetByName('Contacts'))});
      case 'getAccounts':
        return out_({success:true, data:sheetToObjects_(ss.getSheetByName('Accounts'))});
      case 'getProducts':
        return out_({success:true, data:sheetToObjects_(ss.getSheetByName('Products'))});
      case 'getQuotes':
        return out_({success:true, data:sheetToObjects_(ss.getSheetByName('Quotes'))});
      case 'getOrders':
        return out_({success:true, data:sheetToObjects_(ss.getSheetByName('Orders'))});
      default:
        return out_({success:false, error:'Unknown action: '+action});
    }
  } catch(err) {
    return out_({success:false, error:err.toString()});
  }
}

function out_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

function sheetToObjects_(sheet) {
  if (!sheet) return [];
  const data = sheet.getDataRange().getValues();
  const headers = data[0];
  const rows = [];
  for (let i=1;i<data.length;i++) {
    if (!data[i][0]) continue;
    const obj = {};
    for (let j=0;j<headers.length;j++) obj[headers[j]]=data[i][j];
    rows.push(obj);
  }
  return rows;
}
