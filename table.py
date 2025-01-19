import pandas as pd

# Data for the Excel table
data = {
    "Sector": [
        "Courtiers en pétrole"] * 10 + ["Compagnies maritimes"] * 10 +
        ["Raffineries et distributeurs en Afrique"] * 10 +
        ["Compagnies électriques en Afrique"] * 10 +
        ["Associations/Plateformes pétrolières"] * 10 +
        ["Plateformes de négociation"] * 10 +
        ["Maritimes en Afrique"] * 10 +
        ["Compagnies électriques en Asie"] * 10 +
        ["Compagnies électriques en Europe"] * 10,
    "Company Name": [
        "Trafigura", "Vitol", "Glencore", "Gunvor", "Mercuria",
        "Koch Supply & Trading", "BP Trading & Shipping", "Shell Trading", 
        "Chevron Global Trading", "TotalEnergies Trading",
        "Grimaldi Group", "CMA CGM", "MSC", "Maersk Line", "Hapag-Lloyd",
        "Evergreen Marine", "COSCO Shipping", "Yang Ming Marine", "HMM", "ZIM Integrated",
        "SIR", "KPRL", "Sonangol", "NNPC", "GNPC",
        "ZNOC", "TPDC", "PetroSA", "Libya NOC", "EGPC",
        "Eskom", "Sonelgaz", "KenGen", "TANESCO", "ECG",
        "NEPA", "CIE", "STEG", "SENELEC", "EEPCo",
        "ARA", "Petroleum Agency SA", "OPEC", "WAPCo", "IOGP",
        "IPIECA", "AIPN", "OMCs Ghana", "SAPIA", "OGTAN",
        "OilMonster", "Global Oil & Gas Trading", "Platts", "Argus Media", "ICE Futures",
        "DME", "Oilprice", "Nigerian Oil Marketplace", "African Petroleum Exchange", "Asian Oil Marketplace",
        "Grimaldi Group", "CMA CGM", "MSC", "Maersk Line", "PIL",
        "Safmarine", "Africa Express Line", "NileDutch", "Sea Invest", "Spliethoff",
        "NTPC", "CNPC", "KEPCO", "Tata Power", "TEPCO",
        "Adani Power", "Power Grid Corp", "Shanghai Electric", "CLP Holdings", "Energy Dev Corp",
        "EDF", "E.ON", "Enel", "Iberdrola", "RWE",
        "Centrica", "Fortum", "Vattenfall", "Statkraft", "National Grid"
    ],
    "Website": [
        "https://www.trafigura.com", "https://www.vitol.com", "https://www.glencore.com", 
        "https://www.gunvorgroup.com", "https://www.mercuria.com",
        "https://www.ksandt.com", "https://www.bp.com", "https://www.shell.com", 
        "https://www.chevron.com", "https://ts.totalenergies.com",
        "https://www.grimaldi.napoli.it", "https://www.cma-cgm.com", "https://www.msc.com", 
        "https://www.maersk.com", "https://www.hapag-lloyd.com", 
        "https://www.evergreen-marine.com", "https://www.coscoshipping.com", 
        "https://www.yangming.com", "https://www.hmm21.com", "https://www.zim.com",
        "https://www.sir.ci", "https://www.kprl.co.ke", "https://www.sonangol.co.ao", 
        "https://www.nnpcgroup.com", "https://www.gnpcghana.com", 
        "https://www.znoc.co.zm", "https://www.tpdc.co.tz", "https://www.petrosa.co.za", 
        "https://www.noc.ly", "https://www.egpc.com.eg",
        "https://www.eskom.co.za", "https://www.sonelgaz.dz", "https://www.kengen.co.ke", 
        "https://www.tanesco.co.tz", "https://www.ecggh.com",
        "https://www.nepa.gov.ng", "https://www.cie.ci", "https://www.steg.com.tn", 
        "https://www.senelec.sn", "https://www.eepco.gov.et",
        "https://www.afrra.org", "https://www.petroleumagencysa.com", 
        "https://www.opec.org", "https://www.wagpcoghana.com", "https://www.iogp.org", 
        "https://www.ipieca.org", "https://www.aipn.org", "https://www.omcghana.org", 
        "https://www.sapia.org.za", "https://www.ogtan.org",
        "https://www.oilmonster.com", "https://www.globaloilandgastrading.com", 
        "https://www.platts.com", "https://www.argusmedia.com", "https://www.theice.com",
        "https://www.dubaimerc.com", "https://www.oilprice.com", 
        "https://www.nigerianoilmarketplace.com", "https://www.afripetexchange.com", 
        "https://www.asianoilmarketplace.com",
        "https://www.grimaldi.napoli.it", "https://www.cma-cgm.com", "https://www.msc.com", 
        "https://www.maersk.com", "https://www.pilship.com",
        "https://www.safmarine.com", "https://www.africaexpressline.com", 
        "https://www.niledutch.com", "https://www.seainvest.com", 
        "https://www.spliethoff.com",
        "https://www.ntpc.co.in", "https://www.cnpc.com.cn", "https://www.kepco.co.kr", 
        "https://www.tatapower.com", "https://www.tepco.co.jp",
        "https://www.adanipower.com", "https://www.powergrid.in", 
        "https://www.shanghai-electric.com", "https://www.clpgroup.com", 
        "https://www.energy.com.ph",
        "https://www.edf.fr", "https://www.eon.com", "https://www.enel.com", 
        "https://www.iberdrola.com", "https://www.rwe.com",
        "https://www.centrica.com", "https://www.fortum.com", "https://www.vattenfall.com", 
        "https://www.statkraft.com", "https://www.nationalgrid.com"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel
file_path = "Client_Contact_List.xlsx"
df.to_excel(file_path, index=False)
print(f"Excel file saved as: {file_path}")
