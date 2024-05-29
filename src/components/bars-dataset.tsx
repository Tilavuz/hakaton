import { BarChart } from "@mui/x-charts";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import { useTheme } from "./theme-provider";


function BarsDataset() {

  const context = useTheme()
  const darkTheme = createTheme({
    palette: {
      mode: context.theme,
    },
  });

  return (
    <ThemeProvider theme={darkTheme}>
      <BarChart
        xAxis={[
          {
            scaleType: "band",
            data: [
              "Muborak t",
              "Qarshi sh.",
              "Qarshi t",
              "G'uzor t",
              "Dehqonobod",
              "Qamashi t",
              "Kasbi t",
              "Kitob t",
              "Koson t",
              "Mirishkor t",
              "Nishon t",
              "Shaxrisabz sh",
              "Shaxri t",
              "Chiroqchi t",
              "Yakkabog' t",
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
            data: [
              55, 34, 44, 54, 42, 13, 14, 35, 34, 25, 25, 30, 22, 13, 50, 36,
            ],
            label: "Bajarildi",
            color: "#408A7E",
          },
        ]}
        height={400}
      />
    </ThemeProvider>
  );
}

export default BarsDataset;
