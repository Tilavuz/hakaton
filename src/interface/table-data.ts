export interface TableDataProps {
    id: number,
    region: string,
    students?: number,
    english?: number,
    nemis?: number,
    url: string,
}


export interface TableDataNemisProps extends TableDataProps {
    studentsNemis?: number,
    studyingNemis?: number,
    foizNemis?: string ,
    nemisB2?: number,
    nemisC1?: number,
    nemisCertificate?: number,
    foizCertificate?: string,
    nemisCertificateB2?: number,
    nemisCertificateC1?: number,
}