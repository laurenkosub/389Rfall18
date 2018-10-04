section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push    rbp      ;saves the base pointer for the previous function's stack frame
        mov     rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        ;your code goes here!
        
        ;parameters
        ;char *str      rdi 
        ;char val       rsi
        ;int strl       edx
        ;int i          eax
        
        mov     eax, 0          ;int i = 0;
loop1:  cmp     eax, edx        ; i < len ? 
        jge     done1           ; if yes, then continue down, if not then jump to done1

        mov     byte [rdi+rax], sil ;str[i] = val
        
        add     eax, 1  ; i++
        jmp     loop1   ; go back to loop and try again

done1:  leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push    rbp      ;saves the base pointer for the previous function's stack frame
        mov     rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        ;;;;;;;;;;;;;;;;;;;;;
        ;your code goes here!
        ;;;;;;;;;;;;;;;;;;;;;

        ;parameters
        ;char *dst = rdi
        ;char *src = rsi
        ;int len = edx
    
        mov     eax, 0          ;int i = 0 (edx)
loop2:  cmp     eax, edx        ;i < len ?
        jge     done2           ; if yes, then continue down, if not then jump to done2

        mov     bl, byte [rsi + rax]   ;dst[i] = src[i]
        mov     byte [rdi+rax], bl

        add     eax, 1          ;i++
        jmp     loop2           ;jump back to loop 

done2:  leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
