import { Menu } from "lucide-react";
import { ModeToggle } from "./mode-toggle";

export default function Header() {
  return (
    <header className="h-full flex justify-between items-center px-4">
        <div className="">
            <button>
                <Menu size={24}/>
            </button>
        </div>
        <div className="flex items-center gap-4">
          <ModeToggle />
          <div className="flex items-center gap-2 cursor-pointer">
            <div>
              <img width={`60px`} height={`60px`} className="rounded-full" src="https://firebasestorage.googleapis.com/v0/b/total-array-422417-i0.appspot.com/o/logo.png?alt=media&token=ae58c251-6c64-4aca-873b-1b2942b6e9d9" alt="image" />
            </div>
            <div>
              <p className="font-bold">Tilovov Shavqiddin</p>
              <p className="font-thin">329472190471</p>
            </div>
          </div>
        </div>
    </header>
  )
}
