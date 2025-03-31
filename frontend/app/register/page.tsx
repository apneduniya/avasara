import type { Metadata } from "next";

import { constructMetaData } from "@/utils/createMetadata";
import UserRegisterForm from "@/components/form/user-register-form";

export const metadata: Metadata = constructMetaData({
    title: "Register",
    description: "Register for an account",
});


export default function RegisterPage() {
    return (
        <>
            <div className="mt-40 my-20 flex flex-col items-center">
                <h1 className="font-extrabold text-3xl flex flex-col items-center">
                    Create your account
                </h1>
                <p className="text-gray-400 mt-3 max-w-[600px] text-center">
                    You are just a form away from receiving real time opportunities based on your professional profile.
                </p>
                <div className="mt-10 w-full">
                    <UserRegisterForm />
                </div>
            </div>
        </>
    )
}





