def create_features(df):
    df=df.copy()
    df['TotalIncome']=df['ApplicantIncome']+df['CoapplicantIncome']
    df['Income_Loan_Ratio']=df['TotalIncome']/(df['LoanAmount']+1)
    return df