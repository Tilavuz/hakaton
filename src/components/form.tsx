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
<<<<<<< HEAD:src/components/form.jsx
import { useInputStringInvalite } from '../form/useInputStringInvalite'
import {colorBlack, colorFirst,colorRed, colorFormText, hoverColorFirst} from '../constants/style'
=======
>>>>>>> cae7ea0c53a7205ccf3df540b0e936f1d5d1343f:src/components/form.tsx
function FormInput() {
    return (
        <Dialog >
            <DialogTrigger asChild>
                <Button className={`bg-${colorFirst} px-[30px] ml-2 font-[600] hover:bg-${hoverColorFirst} transition-all active:bg-[#183431]`}>O'quvchi qo'shish</Button>
            </DialogTrigger>
            <DialogContent className="lg:max-w-[950px] w-full lg:max-h-[600px] h-full p-8">
                <DialogHeader>
                    <DialogTitle className={`text-${colorFirst} font-[700] text-[1.5rem]`}>O'quvchi qo'shish</DialogTitle>
                    <DialogDescription className='pb-2'>
                        Ma'lumotlarni to'gri kiritishga javobgarligingizni unutmang!
                    </DialogDescription>
                    <hr className={`text-${colorFirst}`}/>
                </DialogHeader>
                <div className={`py-1 flex flex-wrap text-${colorFormText} gap-y-5 gap-x-[20px] justify-between items-center self-center`}>
                    <div className="">
                        <Label htmlFor="lastname" className="text-right">
                            Familiya:
                        </Label>
<<<<<<< HEAD:src/components/form.jsx
                        <Input id="lastname" className={`w-[250px] mt-2 text-${colorBlack}`} placeholder="Familiya" value={lastName.value} onChange={lastName.onChange} />
                        {lastName.color ? null : <span>Familiya faqat harflardan iborat bo'lishi kerak!</span>}
=======
                        <Input id="lastname" className="w-[250px] mt-2 text-black" placeholder="Familiya" />
>>>>>>> cae7ea0c53a7205ccf3df540b0e936f1d5d1343f:src/components/form.tsx
                    </div>
                    <div className="">
                        <Label htmlFor="name" className="text-right">
                            Ism:
                        </Label>
                        <Input id="name" className={`w-[250px] mt-2 text-${colorBlack}`} placeholder="Ism" />
                    </div>
                    <div className="">
                        <Label htmlFor="nickname" className="text-right">
                            Otasining ismi:
                        </Label>
                        <Input id="nickname" className={`w-[250px] mt-2 text-${colorBlack} ring-0 outline-none`} placeholder="Otasining ismi" />
                    </div>
                    <div className="">
                        <Label htmlFor="id" className="text-right">
                            JSHSHIR:
                        </Label>
                        <Input id="id" className={`w-[250px] mt-2 text-${colorBlack}`} placeholder="JSHSHIR" />
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
                        <Input id="photo" className={`w-[250px] mt-2 text-${colorBlack}`} placeholder="Rasmi" type='file' />
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
                        <input className={`border-${colorFirst} checked:bg-${colorFirst} checked:text-${colorFirst}`}type='checkbox' />
                        <Label htmlFor="check" className={`text-right text-${colorFirst}`}>
                            Men hamma ma'lumotlarni to'g'ri kiritganimga ishonchim komil.
                        </Label>
                    </div>

                </div>
                <hr />
                <DialogFooter>
                    <Button className={`bg-${colorRed}`}>Clear</Button>
                    <Button type="submit" className={`bg-${colorFirst}`} disabled>Save</Button>
                </DialogFooter>
            </DialogContent>
        </Dialog>
    )
}

export default FormInput