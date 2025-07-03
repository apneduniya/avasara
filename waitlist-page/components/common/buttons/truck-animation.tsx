/* eslint-disable react-hooks/exhaustive-deps */
"use client";

import { useRef, useState, useEffect } from "react";
import styles from "@/styles/truck-animation.module.css";
import { cn } from "@/lib/utils";


export default function TruckAnimationButton({
    className = "",
    text = "I'm in!",
    successText = "Welcome to the family!",
    handleTimeOut = () => {},
    type = "button",
    startAnimation = true,
    disabled = false,
}: {
    className?: string;
    text?: string;
    successText?: string;
    handleTimeOut?: () => void;
    type?: "button" | "submit" | "reset";
    startAnimation?: boolean;
    disabled?: boolean;
}) {
    const btnRef = useRef<HTMLButtonElement>(null);
    const [isSuccessState, setIsSuccessState] = useState(false);
    const [isDisabled, setIsDisabled] = useState(disabled);

    const handleClick = () => {
        const btn = btnRef.current;
        if (!btn) return;
        if (!btn.classList.contains(styles.animate) && startAnimation) {
            btn.classList.add(styles.animate);
            setTimeout(() => {
                setIsSuccessState(true);
                handleTimeOut();
            }, 7000);
        }
    };

    useEffect(() => {
        setIsDisabled(disabled);
    }, [disabled]);

    useEffect(() => {
        if (startAnimation) {
            handleClick();
        }
    }, [startAnimation]);

    return (
        <button
            ref={btnRef}
            className={cn(styles.order, "rounded-xl", className)}
            type={type}
            onClick={type === "submit" ? handleClick : undefined}
            disabled={isDisabled}
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
