import { RouterProvider, createBrowserRouter } from "react-router-dom"
import { ThemeProvider } from "@/components/theme-provider"
import { Suspense, lazy } from "react"

// Layouts
import RootLayout from "./layouts/root-layout"

// Pages
const ErrorPage = lazy(() => import('./pages/error-page'))
const Profile = lazy(() => import('./pages/profile'))
import Main from "./pages/main"

// Components
import Loader from "./components/loader"


export default function App() {

  const router = createBrowserRouter([
    {
      path: '/',
      element: <RootLayout />,
      errorElement: (
        <Suspense fallback={<Loader />}>
          <ErrorPage />
        </Suspense>
      ),
      children: [
        {
          index: true,
          element: <Main />
        },
        {
          path: 'profile',
          element: <Profile />
        }
      ]
    }
  ])

  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <RouterProvider router={router} />
    </ThemeProvider>
  )
}
