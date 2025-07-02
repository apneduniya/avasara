"use client";

import { useRef, useState } from "react";
import styles from "@/styles/truck-animation.module.css";
import { cn } from "@/lib/utils";


export default function TruckAnimation({
    className = "",
    text = "I'm in!",
    successText = "Welcome to the family!",
    handleTimeOut = () => {},
}: {
    className?: string;
    text?: string;
    successText?: string;
    handleTimeOut?: () => void;
}) {
    const btnRef = useRef<HTMLButtonElement>(null);
    const [isSuccessState, setIsSuccessState] = useState(false);

    const handleClick = () => {
        const btn = btnRef.current;
        if (!btn) return;
        if (!btn.classList.contains(styles.animate)) {
            btn.classList.add(styles.animate);
            setTimeout(() => {
                setIsSuccessState(true);
                handleTimeOut();
            }, 7000);
        }
    };

    return (
        <button
            ref={btnRef}
            className={cn(styles.order, "rounded-xl", className)}
            type="button"
            onClick={handleClick}
        >
            {
                !isSuccessState && (
                    <span className={styles.default}>{text}</span>
                )
            }
            {
                (isSuccessState) && (
                    <span className={styles.success}>
                        {successText}
                        {/* <svg viewBox="0 0 12 10">
                            <polyline points="1.5 6 4.5 9 10.5 1"></polyline>
                        </svg> */}
                    </span>
                )
            }
            <div className={styles.box}></div>
            <div className={styles.truck}>
                <div className={styles.back}></div>
                <div className={styles.front}>
                    <div className={styles.window}></div>
                </div>
                <div className={`${styles.light} ${styles.top}`}></div>
                <div className={`${styles.light} ${styles.bottom}`}></div>
            </div>
            <div className={styles.lines}></div>
        </button>
    );
}
