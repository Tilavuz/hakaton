import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from "@/components/ui/dialog"
import { Button } from "@/components/ui/button"
import {
    Select,
    SelectContent,
    SelectGroup,
    SelectItem,
    SelectTrigger,
    SelectValue,
  } from "@/components/ui/select"
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { useInputStringInvalite } from '../form/useInputStringInvalite'
function FormInput() {
    const lastName = useInputStringInvalite('')
    return (
        <Dialog >
            <DialogTrigger asChild>
                <Button className='bg-[#408a7e] px-[30px] ml-2 font-[600] hover:bg-[#3a6a62] transition-all active:bg-[#183431]'>O'quvchi qo'shish</Button>
            </DialogTrigger>
            <DialogContent className="lg:max-w-[950px] w-full lg:max-h-[600px] h-full p-8">
                <DialogHeader>
                    <DialogTitle className='text-[#408a7e] font-[700] text-[1.5rem]'>O'quvchi qo'shish</DialogTitle>
                    <DialogDescription className='pb-2'>
                        Ma'lumotlarni to'gri kiritishga javobgarligingizni unutmang!
                    </DialogDescription>
                    <hr className='text-[#408a7e] ' />
                </DialogHeader>
                <div className="py-1 flex flex-wrap text-[#868686] gap-y-5 gap-x-[20px] justify-between items-center self-center">
                    <div className="">
                        <Label htmlFor="lastname" className="text-right">
                            Familiya:
                        </Label>
                        <Input id="lastname" className="w-[250px] mt-2 text-black" placeholder="Familiya" value={lastName.value} onChange={lastName.onChange} />
                        {lastName.color ? null : <span>Familiya faqat harflardan iborat bo'lishi kerak!</span>}
                    </div>
                    <div className="">
                        <Label htmlFor="name" className="text-right">
                            Ism:
                        </Label>
                        <Input id="name" className="w-[250px] mt-2 text-black" placeholder="Ism" />
                    </div>
                    <div className="">
                        <Label htmlFor="nickname" className="text-right">
                            Otasining ismi:
                        </Label>
                        <Input id="nickname" className="w-[250px] mt-2 text-black ring-0 outline-none" placeholder="Otasining ismi" />
                    </div>
                    <div className="">
                        <Label htmlFor="id" className="text-right">
                            JSHSHIR:
                        </Label>
                        <Input id="id" className="w-[250px] mt-2 text-black" placeholder="JSHSHIR" />
                    </div>
                    <div className="">
                        <Label htmlFor="phone" className="text-right">
                            Tel. nomer:
                        </Label>
                        <div className='flex gap-[5px]'>
                            <Input id="phoneId" value="+998" className="w-[65px] mt-2" />
                            <Input id="phone" className="w-[180px] mt-2" placeholder="90-123-45-67" />
                        </div>
                    </div>
                    <div className="">
                        <Label htmlFor="photo" className="text-right">
                            Rasmi:
                        </Label>
                        <Input id="photo" className="w-[250px] mt-2 text-black" placeholder="Rasmi" type='file' />
                    </div>
                    <div className="">
                        <Label htmlFor="school" className="text-right">
                            Maktab:
                        </Label>
                        <Input id="school" className="w-[200px] mt-2" placeholder="Maktab" />
                    </div>
                    <div className="">
                        <Label htmlFor="specialty" className="text-right">
                            Yo'nalish:
                        </Label>
                        <Select>
                            <SelectTrigger className="w-[180px]">
                                <SelectValue placeholder="Tanlang..." id='specialty' />
                            </SelectTrigger>
                            <SelectContent>
                                <SelectGroup>
                                    <SelectItem value="english">English</SelectItem>
                                    <SelectItem value="nemis">Nemis</SelectItem>
                                </SelectGroup>
                            </SelectContent>
                        </Select>
                    </div>
                    <div className="">
                        <Label htmlFor="degree" className="text-right">
                            Daraja:
                        </Label>
                        <Select>
                            <SelectTrigger className="w-[180px]">
                                <SelectValue placeholder="Tanlang..." id='specialty' />
                            </SelectTrigger>
                            <SelectContent>
                                <SelectGroup>
                                    <SelectItem value="B1">B1</SelectItem>
                                    <SelectItem value="B2">B2</SelectItem>
                                    <SelectItem value="C1">C1</SelectItem>
                                    <SelectItem value="C2">C2</SelectItem>
                                    <SelectItem value="EILTS9">EILTS 9</SelectItem>
                                </SelectGroup>
                            </SelectContent>
                        </Select>
                    </div>
                    <div className="">
                        <Label htmlFor="status" className="text-right">
                            Holati:
                        </Label>
                        <Select>
                            <SelectTrigger className="w-[180px]">
                                <SelectValue placeholder="Tanlang..." id='specialty' />
                            </SelectTrigger>
                            <SelectContent>
                                <SelectGroup>
                                    <SelectItem value="0">O'qimoqda</SelectItem>
                                    <SelectItem value="'1'">Tugallagan</SelectItem>
                                </SelectGroup>
                            </SelectContent>
                        </Select>
                    </div>
                    <div className="">
                        <Label htmlFor="sertificate" className="text-right">
                            Sertifikat:
                        </Label>
                        <Input id="sertificate" value="" className="w-[200px] mt-2" placeholder="Sertifikat" type='file' disabled />
                    </div>
                    <div className=" flex pt-8 gap-3">
                        <input className='border-[#408a7e] checked:bg-[rgb(64,138,126)] checked:text-[#408a7e]' type='checkbox' />
                        <Label htmlFor="check" className="text-right text-[#408a7e]">
                            Men hamma ma'lumotlarni to'g'ri kiritganimga ishonchim komil.
                        </Label>
                    </div>

                </div>
                <hr />
                <DialogFooter>
                    <Button className='bg-[#E92D47]'>Clear</Button>
                    <Button type="submit" className='bg-[#408a7e]' disabled>Save</Button>
                </DialogFooter>
            </DialogContent>
        </Dialog>
    )
}

export default FormInput