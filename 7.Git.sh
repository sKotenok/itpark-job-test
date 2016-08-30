#Показать команды:
#    создание и переход на новую ветку feature_1
git branch feature_1
git checkout feautre_1

#    сделать два коммита.
git add *
git commit -m "First Commit"
git commit -m "Second Commit"

#    удалить второй коммит вместе с изменениями.
git log
    # commit 7b919 Second Commit
    # commit 8ff4b First Commit
git reset --hard 8ff4b

## Если 2й коммит уже запушен в паблик, взять и отменить его нельзя
git revert 8ff4b
git commit -m "Previous commit was crap, undo it"
git push

#    смержить эту ветку в master.
git checkout master
git merge feature_1

