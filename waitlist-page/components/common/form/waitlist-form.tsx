"use client";

import { useState } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";

import { WaitlistSchema, IWaitlistSchema } from "@/schema/waitlist";
import { WaitlistService } from "@/services/waitlist";

import { cn } from "@/lib/utils";

import WaitlistEmailInput from "@/components/common/form/input/waitlist-email-input";
import TruckAnimationButton from "@/components/common/buttons/truck-animation";
import Confetti from "@/components/common/confetti";


export default function WaitlistForm({ className = "" }: { className?: string }) {
    const [isSuccess, setIsSuccess] = useState(false);
    const [startAnimation, setStartAnimation] = useState(false);
    const [isFormSubmitted, setIsFormSubmitted] = useState(false);

    const waitlistService = new WaitlistService();

    const {
        register,
        handleSubmit,
        setError,
        formState: { errors },
    } = useForm<IWaitlistSchema>({
        resolver: zodResolver(WaitlistSchema),
    });

    // This function will be called when the truck animation is complete
    const handleTimeOut = () => {
        setIsSuccess(true);
    };

    // This function will be called when the form is submitted
    const onSubmit = async (data: IWaitlistSchema) => {
        try {
            setIsFormSubmitted(true);
            setStartAnimation(true);

            const response = await waitlistService.joinWaitlist(data.email);

            if (!response.success) {
                setError("email", { message: response.error });
                return;
            }

        } catch (error) {
            console.error(error);
            setError("email", { message: "Something went wrong. Contact @thatsmeadarsh" });
        }
    };

    return (
        <>
            <div className="flex flex-col gap-4 items-center justify-center">
                <form className={cn("flex flex-col gap-4 md:flex-row items-center justify-center select-none", className)} onSubmit={handleSubmit(onSubmit)}>
                    <WaitlistEmailInput register={register} />
                    <TruckAnimationButton handleTimeOut={handleTimeOut} type="submit" startAnimation={startAnimation} disabled={isFormSubmitted} />
                </form>
                {errors.email && <p className="text-red-700 text-sm">{errors.email.message}</p>}
            </div>
            {isSuccess && <Confetti />}
        </>
    )
}


