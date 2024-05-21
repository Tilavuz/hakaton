import { Menu } from "lucide-react";

export default function Header() {
  return (
    <header className="h-full flex justify-between items-center px-4">
        <div className="">
            <button>
                <Menu size={24}/>
            </button>
        </div>
        <div>

        </div>
    </header>
  )
}
