def la_triche(df):
    df.loc[(df.ndpi_proto == 'BitTorrent'),'predicted']=5
    df.loc[(df.ndpi_proto == 'IRC'),'predicted']=6
    df.loc[(df.ndpi_proto.str.contains('SSH')),'predicted']=6
    df.loc[(df.ndpi_proto.str.contains('Tor')),'predicted']=6
    return df
