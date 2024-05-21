import { BarChart } from "@mui/x-charts";

function BarsDataset() {
  return (
    <BarChart
      xAxis={[
        {
          scaleType: "band",
          data: [
            "Muborak t",
            "Qarshi sh.",
            "Qarshi t",
            "G'uzor t",
            "Dehqanabot",
            "Qamashi t",
            "Kasbi t",
            "Kitob t",
            "Koson t",
            "Mirishkor t",
            "Nishon t",
            "Shaxrisabz sh",
            "Shaxri t",
            "Chiroqchi t",
            "Yakkabog t",
            "Ko'kdala t",
          ],
        },
      ]}
      series={[
        {
          data: [
            75, 64, 54, 84, 82, 43, 54, 55, 74, 65, 75, 90, 82, 43, 100, 63,
          ],
          label: "Maqsadli",
          color: "#FFA048",
        },

        {
          data: [55, 34, 44, 54, 42, 13, 14, 35, 34, 25, 25, 30, 22, 13, 50, 36],
          label: "Bajarildi",
          color: "#408A7E",
        },
      ]}
      
      // margin={{ top: 10, bottom: 30, left: 40, right: 10 }}
      height={400}
    />
  );
}

export default BarsDataset;