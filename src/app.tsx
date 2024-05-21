import { RouterProvider, createBrowserRouter } from "react-router-dom"
import { Suspense, lazy } from "react"

// Layouts
import RootLayout from "./layouts/root-layout"

// Pages
const ErrorPage = lazy(() => import('./pages/error-page'))
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
        }
      ]
    }
  ])

  return <RouterProvider router={router} />
}
