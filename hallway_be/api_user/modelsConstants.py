PLACEHOLDER_MAIL="@magnificamontagna.comunitafvg.it"
PLACEHOLDER_LAN_ID="MC."

MAIN_OFFICE_CHOICES = [
  ('o0', '--'),
  ('o1', 'Informatica'),
  ('o2', 'Ragioneria'),
  ('o3', 'Personale'),
  ('o4', 'Segreteria'),
  ('o5', 'LLPP'),
  ('o6', 'Suap'),
  ('o7', 'Polizia locale'),
  ('o8', 'Politico'),
]
LAN_OFFICE_CHOICES = [
  ('l0', '--'),
  ('l1', 'Pubblica'),
  ('l2', 'Affari Generali'),
  ('l3', 'Ced'),
  ('l4', 'Concorsi'),
  ('l5', 'Direzione'),
  ('l6', 'Pubblica'),
  ('l7', 'Ragioneria'),
  ('l8', 'Risorse Umane'),
  ('l9', 'Scansioni Direzione'),
  ('l10', 'Scansioni Ragioneria'),
  ('l11', 'Scansioni Risorse Umane'),
  ('l12', 'Scansioni Segreteria'),
  ('l13', 'Scansioni Suap'),
  ('l14', 'Scansioni Tecnici'),
  ('l15', 'Suap'),
  ('l16', 'Suap Magnifica Aviano'),
  ('l17', 'Tecnici'),
  ('l18', 'Tributi'),
]
MAIL_OFFICE_CHOICES = [
  ('mo0', '--'),
  ('mo1', 'segreteria@'),
  ('mo2', 'sistemi.informativi@'),
  ('mo3', 'risorseumane@'),
  ('mo4', 'ragioneria@'),
  ('mo5', 'tributi@'),
  ('mo6', '@'),
  ('mo7', '@'),
  ('mo8', '@'),
  ('mo9', '@'),
  ('mo10', '@'),
  ('mo11', '@'),
  ('mo12', '@'),

]
ADWEB_OFFICE_CHOICES = [
  ('ao0', '--'),
  ('ao1', 'Presidente'),
  ('ao2', 'Servizio affari generali, informatica, cultura, sport ed associazioni'),
  ('ao3', 'Servizio associato di polizia locale'),
  ('ao4', 'Servizio associato gestione entrate tributarie'),
  ('ao5', 'Servizio associato gestione risorse umane'),
  ('ao6', 'Servizio gestione risorse economico-finanziarie'),
  ('ao7', 'Servizio gestione territorio, ambiente, lavori pubblici e patrimonio'),
  ('ao8', 'Servizio programmazione, sciluppo territoriale e suap'),
]
GIFRA_OFFICE_CHOICES = [
  ('i0', '--'),
  ('i44', 'POLP  - PO Lavori pubblici'),
]
GIFRA_ROLES_CHOICES = [
  ('i0', '--'),
  ('i1', 'Utente'),
  ('i2', 'Amministratore'),
]
ITERATTI_OFFICE_CHOICES = [
  ('i0', '--'),
  ('i44', 'POLP  - PO Lavori pubblici'),
  ('i20', '-- ALPP, Area lavori pubblici e patrimonio'),
  ('i21', '-- LP, Lavori pubblici'),
  ('i22', '-- PATRIMONIO, Patrimonio'),
  ('i23', '-- MAN, Manutenzione'),
  ('i45', 'POAG  - PO Affari generali'),
  ('i1', '-- AAG, Area affari generali'),
  ('i2', '-- PROT, Protocollo'),
  ('i3', '-- DEL, Delibere'),
  ('i4', '-- BIBLIO, Biblioteca'),
  ('i5', '-- PG, Progetto giovani'),
  ('i6', '-- AANA, Area anagrafe'),
  ('i7', '-- AN, Anagrafe'),
  ('i8', '-- ATTIAN, Atti anagrafe'),
  ('i9', '-- ACA, Area contratti e assicurazioni'),
  ('i10', '-- URP, Urp'),
  ('i11', '-- UFFASS, Ufficio assicurazioni'),
  ('i12', '-- UFFCONT, Ufficio contratti'),
  ('i13', '-- AAGG, Affari generali'),
  ('i46', 'PORAG, PO Ragioneria'),
  ('i14', '-- AEF, Area economico finanziaria'),
  ('i15', '-- RAG, Ragioneria'),
  ('i16', '-- ECON, Economo'),
  ('i17', '-- REVISORI, Revisori'),
  ('i18', '-- TRIB, Tributi'),
  ('i19', '-- INF, Informatica'),
  ('i47', 'POURB, PO Urbanistica'),
  ('i24', '---AUAP, Area urbanistica e attività produttive'),
  ('i25', "-- URB, Urbanistica"),
  ('i26', "-- SUAP, Suap"),
  ('i27', "-- SUE, Sue"),
  ('i28', '-- AMB, Ambiente'),
  ('i29', "-- UFFCOM, Ufficio commercio"),
  ('i48', 'POVIG, PO Vigili'),
  ('i30', '-- AMA, Area messo e albo'),
  ('i31', '-- MESSO, Messo'),
  ('i32', '-- ALBO, Albo'),
  ('i33', '-- ATALBO, Atti albo'),
  ('i33', '-- VIG, Polizia locale'),
  ('i49', 'POCR, PO Casa di riposo'),
  ('i34', '-- CR, Casa di riposo'),
  ('i35', 'UFFSEG - Ufficio segreteria'),
  ('i36', 'SEG - Segretario'),
  ('i37', 'SIND - Sindaco'),
  ('i38', 'GEN  - Protocollo generale'),
  ('i39', 'BASS	- Basso Daniele - assessore'),
  ('i40', 'CREM	- Cremon Martina - assessore'),
  ('i41', 'RAGZ - Ragozzino Giuseppe - assessore'),
  ('i42', 'MEN  - Menegoz Andrea - assessore'),
  ('i43', 'PORAG  - PO Ragioneria'),

]
SDI_ROLES_CHOICES = [
  ('sdi0', '--'),
  ('sdi1', 'FPAVAL - Attive: Valida mette allegati visualizza fatture propria struttura'),
  ('sdi2', 'FPALETT - Attive: Legge fatture propria struttura'),
  ('sdi3', 'FPAFIRMA - Attive: Valida mette allegati e convalida fatture intero ente'),
  ('sdi4', 'FPAGESTLETT - Passive: Visualizza fatture propria struttura'),
  ('sdi5', 'FPASUPER - Passive: Visualizza fatture intero ente'),
  ('sdi6', 'FPASUPERA - Passive: Visualizza e porta in contabilità fatture intero ente'),
  ('sdi7', 'FPASUPERB - Passive: Visualizza porta in contabilità dà esito per fatture intero ente'),
  ('sdi8', 'FPASUPERC - Passive: Visualizza porta in contabilità dà esito e inoltra per fatture intero ente'),
  ('sdi9', 'FPAGESTIONE - Passive: Gestisce fatture propria struttura'),
]
ASCOT_OFFICE_CHOICES = [
  ('a0', '--'),
  ('a1', 'Servizi alla persona e alla comunità'),
  ('a2', 'Servizi demografici'),
  ('a3', 'Servizi educativi e culturali'),
  ('a4', 'Servizio affari generali urp protocollo'),
  ('a5', 'Servizio appalti e contratti'),
  ('a6', 'Servizio turismo sport e associazioni'),
  ('a7', 'Servizio casa di soggiorno anziani'),
  ('a8', 'Servizi informatici'),
  ('a9', 'Servizio contabilità e bilancio'),
  ('a10', 'Servizio tributi'),
]
LAN_ROLES_CHOICES = [
  ('l0', '--'),
  ('l1', 'Utente'),
  ('l2', 'Amministratore'),
  ('l3', 'Solo internet'),
]
WEBSITE_ROLES_CHOICES = [
  ('w0', '--'),
  ('w1', 'Editor'),
  ('w2', 'Amministratore'),
  ('w3', 'Utente area privata'),
]
BOXAPP_ROLES_CHOICES = [
  ('b0', '--'),
  ('b1', 'Utente'),
  ('b2', 'Amministratore'),
]
VOIP_ROLES_CHOICES = [
  ('v0', '--'),
  ('v1', 'Utente'),
  ('v2', 'Amministratore'),
]
MASTERDATA_ROLES_CHOICES = [
  ('m0', '--'),
  ('m1', 'Voce inserita'),
  ('m2', 'Amministratore'),
]
SERVSCOL_ROLES_CHOICES = [
  ('ss0', '--'),
  ('ss1', 'Utente'),
  ('ss2', 'Amministratore'),
]
CRM_ROLES_CHOICES = [
  ('c0', '--'),
  #('c1', 'Utente'),
  ('c2', 'Inserisce richieste'),
]
SUE_ROLES_CHOICES = [
  ('s0', '--'),
  ('s1', 'Utente'),
  ('s2', 'Amministratore'),
]
SUAP_ROLES_CHOICES = [
  ('s0', '--'),
  ('s1', 'Utente'),
  ('s2', 'Amministratore'),
]
AVCP_ROLES_CHOICES = [
  ('a0', '--'),
  ('a1', 'Utente'),
  ('a2', 'Amministratore'),
]
FVGPAY_ROLES_CHOICES = [
  ('f0', '--'),
  ('f1', 'Utente'),
  ('f2', 'Amministratore'),
]
PMPAY_ROLES_CHOICES = [
  ('p0', '--'),
  ('p1', 'Utente'),
  ('p2', 'Amministratore'),
]
MEPA_ROLES_CHOICES = [
  ('m0', '--'),
  ('m1', 'Istruttore'),
  ('m2', 'Punto ordinante'),
]
AGENTR_ROLES_CHOICES = [
  ('a0', '--'),
  ('a1', 'Istruttore'),
  ('a2', 'PO'),
]
ALBOPRET_ROLES_CHOICES = [
  ('ap0', '--'),
  ('ap1', 'Visualizzatore'),
  ('ap2', 'Editor'),
  ('ap3', 'Amministratore'),
]
ADWEB_ROLES_CHOICES = [
  ('a0', '--'),
  ('a1', 'Istruttore'),
  ('a2', 'Istruttore ragioneria'),
  ('a3', 'Istruttore segreteria'),
  ('a5', 'Politico'),
  ('a6', 'Potere di firma'),
]
ITERATTI_ROLES_CHOICES = [
  ('i0', '--'),
  ('i1', 'Utente'),
  ('i2', 'Amministratore'),
]
SDI_OFFICE_CHOICES = [
  ('sdi0', '--'),
  ('sdi1', 'Casa di soggiorno anziani'),
  ('sdi2', 'Risorse umane 2019'),
  ('sdi3', 'Polizia locale'),
  ('sdi4', 'Segreteria generale'),
  ('sdi5', 'Affari generali urp protocollo'),
  ('sdi6', 'Contabilità'),
  ('sdi7', 'Contratti'),
  ('sdi8', 'Cultura biblioteca'),
  ('sdi9', 'Personale'),
  ('sdi10', 'Tributi'),
  ('sdi11', 'Urbanistica ambiente commercio'),
  ('sdi12', 'Ufficio centrale'),
  ('sdi13', 'Manutenzione'),
]
ASCOT_ROLES_CHOICES = [
  ('a0', '--'),
  ('a1', 'Utente'),
  ('a2', 'Amministratore'),
]
AMMTRASP_ROLES_CHOICES = [
  ('at0', '--'),
  ('at1', 'Utente'),
  ('at2', 'Amministratore'),
]
OSSERVATORIO_ROLES_CHOICES = [
  ('o0', '--'),
  ('o1', 'Polizia'),
  ('o2', 'Segretario'),
]



NOTIFICATION = {
  'oggetto': 'Nuova richiesta utente dal gestionale',
  'mittente': 'Gestionale utenti Aviano',
  'destinatario': 'informatica@comune.aviano.pn.it',
}

